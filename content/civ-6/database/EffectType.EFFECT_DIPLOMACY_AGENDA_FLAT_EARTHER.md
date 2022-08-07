---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_FLAT_EARTHER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_FLAT_EARTHER
>
> * Class: `PLAYERS`
> * Parameters:
>	* DiploModForCircumnavigation `Integer`
>	* DiploModPerSpaceProject `Integer`
>	* DiploModPerSpaceport `Integer`
>	* HiddenAgenda `Boolean`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_FLAT_EARTHER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_FLAT_EARTHER",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_FLAT_EARTHER",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_FLAT_EARTHER",
		"DiploModForCircumnavigation",
		"-2"
	),
	(
		"AGENDA_FLAT_EARTHER",
		"DiploModPerSpaceProject",
		"-1"
	),
	(
		"AGENDA_FLAT_EARTHER",
		"DiploModPerSpaceport",
		"-1"
	),
	(
		"AGENDA_FLAT_EARTHER",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_FLAT_EARTHER",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_DESCRIPTION_FLAT_EARTHER"
	),
	(
		"AGENDA_FLAT_EARTHER",
		"StatementKey",
		"AGENDA_FLAT_EARTHER_WARNING"
	),
	(
		"AGENDA_FLAT_EARTHER",
		"TopRankingDiploMod",
		8
	);
	
```

