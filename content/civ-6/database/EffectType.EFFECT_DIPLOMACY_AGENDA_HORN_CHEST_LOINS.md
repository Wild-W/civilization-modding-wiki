---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_HORN_CHEST_LOINS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_HORN_CHEST_LOINS
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* CantBuildDiploMod `Integer`
>	* CorpsPrereqCivic `String`
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_HORN_CHEST_LOINS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_HORN_CHEST_LOINS",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_HORN_CHEST_LOINS",
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
		"AGENDA_HORN_CHEST_LOINS",
		"BottomPercentage",
		30
	),
	(
		"AGENDA_HORN_CHEST_LOINS",
		"BottomRankingDiploMod",
		"-7"
	),
	(
		"AGENDA_HORN_CHEST_LOINS",
		"CantBuildDiploMod",
		"-3"
	),
	(
		"AGENDA_HORN_CHEST_LOINS",
		"CorpsPrereqCivic",
		"CIVIC_NATIONALISM"
	),
	(
		"AGENDA_HORN_CHEST_LOINS",
		"StatementKey",
		"AGENDA_HORN_CHEST_LOINS_WARNING"
	),
	(
		"AGENDA_HORN_CHEST_LOINS",
		"TopPercentage",
		70
	),
	(
		"AGENDA_HORN_CHEST_LOINS",
		"TopRankingDiploMod",
		6
	);
	
```

