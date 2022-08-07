---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_ARCHIPELAGIC_STATE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_ARCHIPELAGIC_STATE
>
> * Class: `PLAYERS`
> * Parameters:
>	* AcceptableIslandPercentage `Integer`
>	* MaxNegativeModifier `Integer`
>	* MaxPositiveModifier `Integer`
>	* MaxTilesLargeIsland `Integer`
>	* MaxTilesMediumIsland `Integer`
>	* MaxTilesSmallIsland `Integer`
>	* ReductionTurns `Integer`
>	* StatementKey `String`

## Samples

```SQL {title="AGENDA_ARCHIPELAGIC_STATE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_ARCHIPELAGIC_STATE",
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
		"AGENDA_ARCHIPELAGIC_STATE",
		"AcceptableIslandPercentage",
		20
	),
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"MaxNegativeModifier",
		"-8"
	),
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"MaxPositiveModifier",
		8
	),
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"MaxTilesLargeIsland",
		37
	),
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"MaxTilesMediumIsland",
		19
	),
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"MaxTilesSmallIsland",
		7
	),
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"ReductionTurns",
		2
	),
	(
		"AGENDA_ARCHIPELAGIC_STATE",
		"StatementKey",
		"AGENDA_ARCHIPELAGIC_STATE_WARNING"
	);
	
```

