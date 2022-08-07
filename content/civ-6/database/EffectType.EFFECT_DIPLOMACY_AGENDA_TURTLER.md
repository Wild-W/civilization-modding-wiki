---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_TURTLER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_TURTLER
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomRankingDiploMod `Integer`
>	* HiddenAgenda `Boolean`
>	* SimpleModifierDescription `String`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_TURTLER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_TURTLER",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_TURTLER",
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
		"AGENDA_TURTLER",
		"BottomRankingDiploMod",
		"-6"
	),
	(
		"AGENDA_TURTLER",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_TURTLER",
		"SimpleModifierDescription",
		"AGENDA_TURTLER_WARNING"
	),
	(
		"AGENDA_TURTLER",
		"TopRankingDiploMod",
		4
	);
	
```

