---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_YIELD_CHANGE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="SETTLEMENT_EMERGENCY_MEMBER_GPT_REWARD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SETTLEMENT_EMERGENCY_MEMBER_GPT_REWARD",
		"MODIFIER_EMERGENCY_PLAYERS_YIELD_PER_TURN",
		"SETTLEMENT_EMERGENCY_MEMBER_GPT_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SETTLEMENT_EMERGENCY_MEMBER_GPT_REWARD",
		"Amount",
		1
	),
	(
		"SETTLEMENT_EMERGENCY_MEMBER_GPT_REWARD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

