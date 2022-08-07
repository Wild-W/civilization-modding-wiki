---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_EMBARK_UNIT_PASS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_EMBARK_UNIT_PASS
>
> * Class: `Unknown`
> * Parameters:
>	* UnitType `Unknown`

## Samples

```SQL {title="TRAIT_TRADER_EARLY_EMBARK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_TRADER_EARLY_EMBARK",
		"MODIFIER_PLAYER_ADJUST_EMBARK_UNIT_PASS",
		"PLAYER_HAS_FOREIGN_TRADE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TRADER_EARLY_EMBARK",
		"UnitType",
		"UNIT_TRADER"
	);
	
```

