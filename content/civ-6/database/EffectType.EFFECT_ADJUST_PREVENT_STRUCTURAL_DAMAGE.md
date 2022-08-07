---
tags:
- EffectType
title: EFFECT_ADJUST_PREVENT_STRUCTURAL_DAMAGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PREVENT_STRUCTURAL_DAMAGE
>
> * Class: `CITIES`
> * Parameters:
>	* Prevent `Boolean`

## Samples

```SQL {title="REINFORCED_INFRASTRUCTURE_PREVENET_STRUCTURAL_DAMAGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"REINFORCED_INFRASTRUCTURE_PREVENET_STRUCTURAL_DAMAGE",
		"MODIFIER_GOVERNOR_ADJUST_PREVENET_STRUCTURAL_DAMAGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"REINFORCED_INFRASTRUCTURE_PREVENET_STRUCTURAL_DAMAGE",
		"Prevent",
		1
	);
	
```

