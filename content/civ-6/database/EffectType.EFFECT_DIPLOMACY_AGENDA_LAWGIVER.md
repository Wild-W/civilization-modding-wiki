---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_LAWGIVER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_LAWGIVER
>
> * Class: `PLAYERS`
> * Parameters:
>	* BonusIfNotOriginalOwner `Integer`
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples
```SQL {title="AGENDA_LAWGIVER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_LAWGIVER",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_LAWGIVER",
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
		"AGENDA_LAWGIVER",
		"BonusIfNotOriginalOwner",
		50
	),
	(
		"AGENDA_LAWGIVER",
		"BottomPercentage",
		30
	),
	(
		"AGENDA_LAWGIVER",
		"BottomRankingDiploMod",
		"-8"
	),
	(
		"AGENDA_LAWGIVER",
		"StatementKey",
		"AGENDA_LAWGIVER_WARNING"
	),
	(
		"AGENDA_LAWGIVER",
		"TopPercentage",
		65
	),
	(
		"AGENDA_LAWGIVER",
		"TopRankingDiploMod",
		8
	);
	
```

