---
tags:
- EffectType
title: EFFECT_ATTACH_MODIFIER_IF_PROMOTION_CLASS_MATCHES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ATTACH_MODIFIER_IF_PROMOTION_CLASS_MATCHES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* ModifierId `String`
>		* Attach a modifier of the specified ID to the units matching the specified UnitPromotionClassType

## Samples

```SQL {title="APPLY_RES_UNIT_COMBAT_DEBUFF"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APPLY_RES_UNIT_COMBAT_DEBUFF",
		"MODIFIER_ALL_UNITS_APPLY_MODIFIER_IF_PROMOTION_CLASS_MATCHES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APPLY_RES_UNIT_COMBAT_DEBUFF",
		"Amount",
		"WC_RES_UNIT_COMBAT_DEBUFF"
	);
	
```


```SQL {title="APPLY_RES_UNIT_COMBAT_BUFF"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APPLY_RES_UNIT_COMBAT_BUFF",
		"MODIFIER_ALL_UNITS_APPLY_MODIFIER_IF_PROMOTION_CLASS_MATCHES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APPLY_RES_UNIT_COMBAT_BUFF",
		"ModifierId",
		"WC_RES_UNIT_COMBAT_BUFF"
	);
	
```

