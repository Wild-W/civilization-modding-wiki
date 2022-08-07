---
tags:
- EffectType
title: EFFECT_DIPLOMACY_ONE_SIDED_TRADES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_ONE_SIDED_TRADES
>
> * Class: `PLAYERS`
> * Parameters:
>	* IncrementValue `Integer`
>	* MaxValue `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* TradeValuePerModifierPoint `Integer`

## Samples

```SQL {title="STANDARD_DIPLOMATIC_ONE_SIDED_TRADES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_ONE_SIDED_TRADES",
		"MODIFIER_PLAYER_DIPLOMACY_ONE_SIDED_TRADES",
		"ON_DEAL_ENACTED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_ONE_SIDED_TRADES",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_ONE_SIDED_TRADES",
		"MaxValue",
		20
	),
	(
		"STANDARD_DIPLOMATIC_ONE_SIDED_TRADES",
		"ReductionTurns",
		2
	),
	(
		"STANDARD_DIPLOMATIC_ONE_SIDED_TRADES",
		"ReductionValue",
		1
	),
	(
		"STANDARD_DIPLOMATIC_ONE_SIDED_TRADES",
		"TradeValuePerModifierPoint",
		10
	);
	
```

