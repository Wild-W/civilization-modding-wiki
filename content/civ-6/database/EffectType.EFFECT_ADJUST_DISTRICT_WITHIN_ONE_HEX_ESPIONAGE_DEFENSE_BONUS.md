---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_WITHIN_ONE_HEX_ESPIONAGE_DEFENSE_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_WITHIN_ONE_HEX_ESPIONAGE_DEFENSE_BONUS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples
```SQL {title="DIPLOMATIC_QUARTER_ESPIONAGE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DIPLOMATIC_QUARTER_ESPIONAGE_BONUS",
		"MODIFIER_DISTRICT_ADJUST_WITHIN_ONE_HEX_ESPIONAGE_DEFENSE_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DIPLOMATIC_QUARTER_ESPIONAGE_BONUS",
		"Amount",
		2
	);
	
```

