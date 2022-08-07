---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_PATRON_OF_ARTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_PATRON_OF_ARTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples
```SQL {title="AGENDA_PATRON_OF_ARTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_PATRON_OF_ARTS",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_PATRON_OF_ARTS",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_PATRON_OF_ARTS",
		"BottomPercentage",
		30
	),
	(
		"AGENDA_PATRON_OF_ARTS",
		"BottomRankingDiploMod",
		8
	),
	(
		"AGENDA_PATRON_OF_ARTS",
		"StatementKey",
		"AGENDA_PATRON_OF_ARTS_WARNING"
	),
	(
		"AGENDA_PATRON_OF_ARTS",
		"TopPercentage",
		65
	),
	(
		"AGENDA_PATRON_OF_ARTS",
		"TopRankingDiploMod",
		"-8"
	);
	
```

