---
tags:
- EffectType
title: EFFECT_ADJUST_FEATURE_NO_IMPROVEMENT_APPEAL_GOVERNOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FEATURE_NO_IMPROVEMENT_APPEAL_GOVERNOR
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="FORESTRY_MANAGEMENT_FEATURE_NO_IMPROVEMENT_APPEAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FORESTRY_MANAGEMENT_FEATURE_NO_IMPROVEMENT_APPEAL",
		"MODIFIER_GOVERNOR_ADJUST_FEATURE_NO_IMPROVEMENT_APPEAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FORESTRY_MANAGEMENT_FEATURE_NO_IMPROVEMENT_APPEAL",
		"Amount",
		1
	);
	
```

